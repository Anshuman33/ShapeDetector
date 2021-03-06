;(function (){
    
    var canvas, ctx;
    
    var draw = false;
    var currX, currY, prevX, prevY = 0;
    var color = 'black', thickness = 3;

    // Function to initialize the canvas and context variable
    function init(){
        

        canvas = document.getElementById("#canvas1");
        ctx = canvas.getContext('2d')
        ctx.fillStyle = "white";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        canvas.addEventListener("mousedown", function(e){
            updatePositions(e);
            draw = true;
        })

        canvas.addEventListener("mouseout", function(e){
            updatePositions(e);
            draw = false;
        });

        canvas.addEventListener("mousein", function(e){
            updatePositions(e);
            draw = true;
        });

        canvas.addEventListener("mousemove",function(e){
            updatePositions(e);
            if (draw == true){ 
                drawPixel();
                //console.log(e.offsetX, e.offsetY);
            }
        })

        canvas.addEventListener("mouseup", function(e){
            updatePositions(e);
            draw = false;
        });

    }

    function drawPixel(){
        
        ctx.beginPath();
        ctx.moveTo(prevX, prevY);
        ctx.lineTo(currX, currY);
        ctx.strokeStyle = color || '#000';
        ctx.lineWidth = thickness;
        ctx.stroke();
        ctx.closePath()
    }

    function updatePositions(event){
        prevX = currX;
        prevY = currY;
        currX = event.offsetX;
        currY = event.offsetY;
    }
    

    // wait for HTML to load
    document.addEventListener("DOMContentLoaded", init);

})()

function clearCanvas(){
    var canvas = document.getElementById("#canvas1");
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function predictImage(){

    // Get the base64 string for image
    var canvas = document.getElementById("#canvas1");
    var imgDataStr = canvas.toDataURL("image/png")  
    
    var request = new XMLHttpRequest();

    request.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            alert(this.responseText);
        }
    }
    
    request.open('POST', "/predict", true);
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send("imgData=" + imgDataStr);

}
