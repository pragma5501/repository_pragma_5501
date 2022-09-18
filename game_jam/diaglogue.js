export class Dialogue {
    constructor(character, mode) {
        this.img = new Image();
        console.log("mode: "+mode);
        if(character == "enemy" && mode == 0) {
            this.srcs = [
                './dialogue_image_folder/kill_manyu.png',
                './dialogue_image_folder/disgusting_monster.png',
            ];
        } 
        else if( character == "enemy" && mode == 1) {
            this.srcs = [
                './dialogue_image_folder/manyu_kill_people.png',
            ];
        } 
        else if(character == "enemy" && mode == 2) {
            this.srcs = [
                './dialogue_image_folder/mon..monster.png',
            ];
        }

        else if(character == "enemy" && mdoe == 3) {
            this.srcs = [
                ''
            ];
        }
        

        else if( character == "user"  && mode == 0) {
            console.log("make");
            this.srcs = [
                './dialogue_main_folder/help_me.png',
                './dialogue_main_folder/nan_manyu_not.png',
                
            ];
        } 

        else if( character == "user"  && mode == 1) {
            this.srcs = [
                './dialogue_main_folder/kimi_want.png',
            ];
        }
        else if( character == "user"  && mode == 2) {
            this.srcs = [
                './dialogue_main_folder/kimi_want.png',
                './dialogue_main_folder/watasi_manyu.png',
            ];
        }
        else if( character == "user"  && mode == 3) {
            this.srcs = [

            ];
        }
        this.img.src = this.srcs[ Math.floor(Math.random() * this.srcs.length) ];

        this.dialogueWidth = 150;
        this.dialogueHeight = 200;

        this.count = 0;
    }
    draw(ctx,x,y) {
        this.animate(ctx,x,y);
    }
    animate(ctx, x, y) {
        this.count++;
        if(this.count == 50) {
            return false;
        }
        ctx.save()
        ctx.translate(x, y);
        ctx.drawImage(
            this.img,
            -this.dialogueWidth/2,
            -this.dialogueHeight/2 - 100,
            this.dialogueWidth,
            this.dialogueHeight,
        );
        ctx.restore();
        return true;
    }
    
}