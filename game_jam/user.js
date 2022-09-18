import { Slime } from "./slime.js";

export class User {
    constructor(hp, attack_damage, defense, nickname) {
        this.hp = hp;
        this.attack_damage = attack_damage;
        this.defense = defense;
        this.killScore = 0;
        this.liveScore = 0;
        
        this.make_slime();
        
        this.mode = 0;
    }

    resize(stageWidth, stageHeight) { 
        this.stageWidth = stageWidth;
        this.stageheight = stageHeight;

        this.x = stageWidth / 2;
        this.y = stageHeight / 2;
        this.slime.resize(this.x, this.y);
    }
    setMode() {
        this.slime.setMode(this.mode);
    }
    make_slime() {
        this.slime = new Slime(this.stageWidth);
    }

    draw(ctx, dots) {
 
        this.slime.draw(ctx, dots);
    }
    //player_controller
    jump() {
        this.slime.jump();
    }
    move(direction) {
        this.slime.move(direction);
    }
    fire() {
        if(this.mode >= 1) {
            this.slime.fire();
        }   
    }
    rotate(direction) {
        this.slime.rotate(direction);
    }
    stopRotate() {
        this.slime.stopRotate();
    }
    returnX() {
        return this.slime.returnX();
    }
    returnY() {
        return this.slime.returnY();
    }
    getCollisionRadius() {
        return this.slime.getCollisionRadius();
    }
}
