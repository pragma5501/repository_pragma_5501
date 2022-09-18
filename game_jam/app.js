
import { Enemygroup } from "./enemygroup.js";
import { Hill } from "./hill.js";
import { User } from "./user.js";

class App {
    constructor() {
        
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        document.body.appendChild(this.canvas);
        
        //make hill
        this.hills = [
            new Hill('#06c258', 0.2, 12),
            new Hill('#06a94d', 0.5, 8),
            new Hill('#059142', 1.4, 6),
        ];


        //make user
        this.user = new User(3,0, 0, "slime");

        //make Enemies
        this.enemygroup = new Enemygroup();
        this.enemyCount = 4;
        this.enemygroup.makeEnemies(4, 0);

        window.addEventListener('resize', this.resize.bind(this), false);

        //resize_part
        this.pixelRatio = window.devicePixelRatio > 1 ? 2 : 1;
        this.resize();
        
        requestAnimationFrame(this.animate.bind(this));

        this.keyboardAscii = {
            SPACE: 32,
            W: 87,
            A: 65,
            S: 83,
            D: 68,
            R: 82,
        }   
        //user.killScore에 따른 스테이지
        this.gameStage = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
        }
        document.addEventListener("keydown", this.keyDownHandler.bind(this), false);
        
    }
    keyDownHandler(e) {
        //console.log(e);
        if(e.keyCode == this.keyboardAscii.SPACE) {
            this.user.jump();
        }

        if(e.keyCode == this.keyboardAscii.A) {
            this.user.rotate(-1);
            this.user.move(-1)
        }
        if(e.keyCode == this.keyboardAscii.D) {
            this.user.rotate(1);
            this.user.move(1);
        }  
        if(e.keyCode == this.keyboardAscii.S) {
            this.user.stopRotate();
        }
    }
    
    resize() {
        this.stageWidth = document.body.clientWidth;
        this.stageHeight = document.body.clientHeight;

        this.canvas.width = this.stageWidth * this.pixelRatio;
        this.canvas.height = this.stageHeight * this.pixelRatio;

        this.ctx.scale(this.pixelRatio, this.pixelRatio);

        for(let i = 0; i < this.hills.length; i++) {
            this.hills[i].resize(this.stageWidth, this.stageHeight);
        }

        //user resize
        this.user.resize(this.stageWidth, this.stageHeight);
    
        //enemy resize
        this.enemygroup.resize(this.stageWidth, this.stageHeight);
        
    }

    animate(t) {
        requestAnimationFrame(this.animate.bind(this));
        this.ctx.clearRect(0, 0, this.stageWidth, this.stageHeight);

        //draw score_text

        this.ctx.font = '48px serif';
        this.ctx.fillText(this.user.killScore+" kill\n"+this.user.liveScore+" avoid", 10, 50);
        //draw stage_text
        this.ctx.font = '48px serif';
        this.ctx.fillText(this.user.mode+" stage", this.stageWidth - 300, 50);
        this.ctx.fillText(this.user.hp + " hp", this.stageWidth - 200,  98 );
        let dots;
        for (let i = 0; i < this.hills.length; i++) {
            dots = this.hills[i].draw(this.ctx);
        }
        
        //draw user
        this.user.draw(this.ctx, dots);
        
        //judge game mode
        this.user.mode = Math.floor(this.user.killScore / 10);
        this.user.setMode();
        if( this.user.mode == 3) {
            return;
        }
        

        //reset enemy
        if( this.enemyCount == 0)  {

            this.enemygroup = new Enemygroup();

            let newTotalEnemy = Math.floor( Math.random() * 5) + 2;
            this.enemyCount = newTotalEnemy;
            this.enemygroup.makeEnemies(newTotalEnemy, this.user.mode);
            this.enemygroup.resize(this.stageWidth, this.stageHeight);
            
        }
        //draw enemy
        for(let i = 0; i < this.enemygroup.totalEnemy; i++) {
            this.enemygroup.draw(this.ctx, dots);
        }

        this.detectTotalCollision();
        this.checkEnding();
    }


    //간단하게 원으로 충돌판정 구현
    detectCollision(classObject1, classObject2) {
        let classObject1_radius = classObject1.getCollisionRadius();
        let classObject2_radius = classObject2.getCollisionRadius();

        let classObject1_x = classObject1.returnX();
        let classObject1_y = classObject1.returnY();
        
        let classObject2_x = classObject2.returnX();
        let classObject2_y = classObject2.returnY();
        let distancePow2 = (classObject1_x - classObject2_x)**2 + (classObject1_y - classObject2_y)**2;
        
        if(distancePow2 < (classObject1_radius + classObject2_radius) ** 2 ) {
            
            return true;
        }
        
        return false;
    }
    
    detectTotalCollision() {
        
        if( this.user.returnX() < this.user.slime.slimeWidth/2) {
            this.user.move(1);
        }
        if( this.user.returnX() > this.stageWidth + this.user.slime.slimeWidth/2 ) {
            this.user.move(-1);
        }
        for(let i = 0; i < this.enemygroup.totalEnemy; i++) {
            if(this.enemygroup.enemies[i].status.alive == false) {
                continue;
            }
            //user와 enemies 충돌판정
            let collisionJudge = this.detectCollision(this.enemygroup.enemies[i], this.user); 
            
            //유저와 부딪힌거
            if(collisionJudge == true && this.enemygroup.enemies[i].status.alive == true) {
                if(collisionJudge == true && this.user.slime.rotateJudge == false) {
                    console.log(this.user.slime.rotateJudge);
                    this.user.hp -= 1;
                }
                this.enemygroup.enemies[i].status.alive = false;
                this.enemyCount -= 1;
                this.user.killScore += 1;
            }

            //벽 밖으러 나간거
            else if( this.enemygroup.enemies[i].returnX() < 0 && this.enemygroup.enemies[i].direction == -1) {
                this.enemygroup.enemies[i].status.alive = false;
                this.enemyCount -= 1;
                this.user.liveScore += 1;
            }
            else if( this.enemygroup.enemies[i].returnX() > this.stageWidth && this.enemygroup.enemies[i].direction == 1) {
                this.enemygroup.enemies[i].status.alive = false;
                this.enemyCount -= 1;
                this.user.liveScore += 1;
            }
            console.log("enemyCount: " + this.enemyCount);
        }
    }
    checkEnding() {
        if( this.user.mode==0 && this.user.liveScore >= 100) {
            document.location.href='./ending1.html';
        }
        if( this.user.mode==1 && this.user.liveScore >= 70) {
            document.location.href= './ending2.html';
        }
        if( this.user.mode==2 && this.user.liveScore >= 50) {
            document.location.href = './ending3.html';
        }
        if( this.user.hp <= 0) {
            document.location.href ='./ending5.html';
        }
        if( this.user.killScore >= 30) {
            document.location.href ='./ending4.html';
        }
        
    }
}

window.onload = () => {

    new App();
    let audio = new Audio('./music_folder/music1.mp3');
    audio.play();
    audio.loop = true;
    
};
