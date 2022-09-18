import { Dialogue } from "./diaglogue.js";

export class Enemy {
    //**Direction must be 1 or -1 , 디렉션이 1이면 왼쪽, -1이면 오른쪽 */
    constructor(src, direction, mode) {
        this.direction = direction;

        this.img = new Image();
        this.img.src = src;

        this.imgWidth = 200;
        this.imgHeight = 200;

        this.enemyWidth  = 100;
        this.enemyHeight = 100;

        this.enemyWidthHalf = this.enemyWidth / 2;


        this.speed = Math.random() * 1 + 1;
        this.cur = 0;

        
        this.status = {
            alive: true,
        };
        this.hasDialogue = Math.floor( Math.random() * 10 ) + 1; 
        if(this.hasDialogue == 7) {
            this.dialogue = new Dialogue("enemy", mode);
        }
        this.count = 0;
    }

    resize(stageWidth, stageHeight) {
        console.log('resize');
        this.stageWidth = stageWidth;
        this.stageHeight = stageHeight;
        //set_init_position
        if(this.direction == -1) {
            this.x = stageWidth;
        }
        else {
            this.x = 0;
        }
    }

    returnX() {
        return this.x + this.enemyWidth/2;
    }
    returnY() {
        return this.y + this.enemyHeight/2;
    }
    getCollisionRadius() {
        return this.enemyWidthHalf;
    }

    draw(ctx, dots) {
        this.animate(ctx, dots);
    }

    animate(ctx, dots) {
        //position, direction = 1 or -1

        this.count++;
        if(this.count == 40 && this.enemyHeight == 100) {
            this.enemyHeight += 20;
            this.count = 0;
        }
        else if(this.count == 40 && this.enemyHeight == 120) {
            this.enemyHeight -= 20;
            this.count = 0;
        }
        this.x = this.x + this.speed * this.direction;

        const closest = this.getY(this.x, dots);
        this.y = closest.y;

        //draw dialogue
        if(this.hasDialogue == 7) {
            this.dialogue.draw(ctx, this.x, this.y);
        }
        //draw black box
        ctx.save(); 
        ctx.translate(this.x, this.y);

        //drawImage(image, dx, dy, dWidth, dHeight)

        ctx.drawImage(
            this.img,
            -this.enemyWidthHalf,
            -this.enemyHeight + 20,
            this.enemyWidth,
            this.enemyHeight,
        );
        ctx.restore();
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