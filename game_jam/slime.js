import { Dialogue } from "./diaglogue.js";

export class Slime {
    constructor(stageWidth) {
        this.img = new Image();
        this.img.src='./image_folder/main_character.png';
        
        this.imgWidth = 200;
        this.imgHeight = 200;

        this.slimeWidth  = 50;
        this.slimeHeight = 50;

        this.slimeWidthHalf = this.slimeWidth / 2;
        this.x = stageWidth;
        
        this.speed = 10;
        this.speedBack = 2;
        this.cur = 0;

        //jump space
        this.jumpJudge = false;
        this.jumpSpeed = 300;

        this.rotateJudge = false;

        this.count = 0;
        
    }
    
    resize(x, y) {
        this.x = x;
        this.y = y;
        this.basicX = x;
    }
    setMode(mode) {
        this.mode = mode;
    }
    //controll_space
    jump() {
        if(this.jumpJudge==true) return;
        this.jumpJudge = true;
        this.jumpSinTheta = 0;
        this.jumpStartY = this.y;
        this.changeImage("worried_character")
        console.log("jump")
    }
    //controll_a_d
    move(direction) {
        this.moveJudge = true;
        this.moveDirection = direction;
    }
    //controll_k 
    fire() {

    }
    //controll_r
    rotate(direction) {
        if(this.rotateJudge == false) {
            this.rotateTheta = 0;
        };
        this.rotateDirection = direction;
        this.rotateJudge = true;
        
    }
    stopRotate() {
        this.rotateJudge = false;
        this.moveJudge = false;
    }
    returnX() {
        return this.x + this.slimeWidth/2;
    }
    returnY() {
        return this.y + this.slimeHeight/2;
    }
    getCollisionRadius() {
        return this.slimeWidthHalf;
    }
    draw(ctx, dots) {
        this.animate(ctx, dots);
        
    }

    animate(ctx, dots) {
        if(this.moveJudge == true) {
            this.x += this.speed * this.moveDirection;
        } 
        else{
            if( this.x < this.basicX) {
                this.x += this.speedBack;
            } 
            else if( this.x > this.basicX) {
                this.x -= this.speedBack;
            }
        }
        
        //position + jump
        const closest = this.getY(this.x, dots);
        this.y = closest.y;
        if(this.jumpJudge == true) {
            this.y = this.jumpStartY - Math.sin( this.jumpSinTheta ) * this.jumpSpeed;
            //체공시간 조절, math.pi / n, n이 높아질수록 체공시간이 길어짐
            this.jumpSinTheta += Math.PI / 60;
            
            if(this.jumpSinTheta > Math.PI || this.y > closest.y  +20 ) {
                this.changeImage("basic_character");
                this.jumpJudge = false;
            }

        }

        //draw dialogue
        this.count++;
        if(this.count == 100) {
            this.dialogue = new Dialogue("user", this.mode);
        }
        if( 200 > this.count && this.count > 100) {
            
            this.dialogue.draw(ctx, this.x, this.y);
        }
        if(this.count == 500) {
            this.count = 0;
        }


        //draw
        ctx.save();
        ctx.translate(this.x, this.y);

        //drawImage(image, dx, dy, dWidth, dHeight)
        if( this.rotateJudge == true) {
            ctx.rotate(this.rotateTheta );
            //rotate_speed
            //  console.log(this.rotateTheta);
            this.rotateTheta += 18 * Math.PI / 180 * this.rotateDirection;
            
            
            ctx.drawImage(
                this.img,
                -this.slimeWidthHalf,
                -this.slimeHeight / 2,
                this.slimeWidth,
                this.slimeHeight,
            );
        }
        else {
            
            ctx.drawImage(
                this.img,
                -this.slimeWidthHalf,
                -this.slimeHeight + 20,
                this.slimeWidth,
                this.slimeHeight,
            );
        }   
        ctx.restore();
    }
    changeImage(characterPngName) {
        this.imageSrcs = {
            basic_character:'./image_folder/main_character.png',
            worried_character:'./image_folder/main_character_worried.png',
        }
        this.img.src = this.imageSrcs[characterPngName];

    }

    getY(x, dots) {
        for (let i = 1; i < dots.length; i++) {
            if (x >= dots[i].x1 && x <= dots[i].x3) {
                return this.getY2(x, dots[i]);
            }
        }

        return {
            y: 0,
            rotation: 0,
        };
    }

    getY2(x, dot) {
        const total = 200;
        let pt = this.getPointOnQuad(
            dot.x1,
            dot.y1,
            dot.x2,
            dot.y2,
            dot.x3,
            dot.y3,
            0
        );
        let prevX = pt.x;

        for (let i = 1; i < total; i++) {
            const t = i / total;
            pt = this.getPointOnQuad(
                dot.x1,
                dot.y1,
                dot.x2,
                dot.y2,
                dot.x3,
                dot.y3,
                t
            );

            if (x >= prevX && x <= pt.x) {
                return pt;
            }
            prevX = pt.x;
        }

        return pt;
    }

    getQuadValue(p0, p1, p2, t) {
        return (1 - t) * (1 - t) * p0 + 2 * (1 - t) * t * p1 + t * t * p2;
    }

    getPointOnQuad(x1, y1, x2, y2, x3, y3, t) {
        const tx = this.quadTangent(x1, x2, x3, t);
        const ty = this.quadTangent(y1, y2, y3, t);
        const rotation = -Math.atan2(tx, ty) + (90 * Math.PI) / 180;
        return {
            x: this.getQuadValue(x1, x2, x3, t),
            y: this.getQuadValue(y1, y2, y3, t),
            rotation,
        };
    }

    quadTangent(a, b, c, t) {
        return 2 * (1 - t) * (b - a) + 2 * (c - b) * t;
    }
    
}