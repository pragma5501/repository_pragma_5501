import { Enemy } from "./enemy.js";

export class Enemygroup {
    constructor() {
        this.totalEnemy = 0;
        
        this.srcs = [
            './image_folder/enemy_red.png',
            './image_folder/enemy_green.png',
            './image_folder/enemy_blue.png',
        ];

        console.log("새로만듬");

    }
    
    makeEnemies(totalEnemy, mode) {
        this.totalEnemy = totalEnemy;
        this.enemies = [];
        for(let i = 0; i < this.totalEnemy; i++) {
            const enemy = new Enemy(this.getRandomSrc(), this.getRandomDirection(), mode);
            this.enemies[i] = enemy;
            
        }
    }

    resize(stageWidth, stageHeight) {
        for(let i = 0; i < this.totalEnemy; i++) {
            const enemy = this.enemies[i];
            enemy.resize(stageWidth, stageHeight);
        }
    }

    draw(ctx, dots) {
        for(let i = 0; i < this.totalEnemy; i++) {
            
            const enemy = this.enemies[i];
            if(enemy.status.alive == true)  enemy.draw(ctx, dots);
           
        }
    }

    getRandomSrc() {
        let min = Math.ceil(0);
        let max = Math.floor(this.srcs.length);

        return this.srcs[Math.floor(Math.random() * (max - min)) + min];
    }

    getRandomDirection() {
        let min = Math.ceil(0);
        let max = Math.floor(2);
        let direction = Math.floor(Math.random() * (max - min)) + min;

        if( direction == 0) {
            return -1;
        }
        if( direction == 1) {
            return 1;
        }
    }

}