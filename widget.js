function addTfWidget(x, y, left=false) {
    var node = document.createElement("div");
    var text = document.createTextNode("Click here for TF");
    node.appendChild(text);
    node.style.position = "fixed";
    if(left){
        node.style.right = x + "px"; // align left
    }else{
        node.style.left = x + "px";
    }
   

    node.style.top =  y + "px";
    node.style.zIndex = 999998;
    node.style.backgroundColor = "#CCCCCC";
    node.style.width = 200;
    node.style.height = 100;
    node.style.display = "table-cell";
    node.style.textAlign = "center";
    node.style.verticalAlign = "middle";

    node.onclick = function () {
        var iframe = document.createElement("iframe");
        iframe.src = "http://localhost:8080"
        iframe.style.position = "fixed";
        iframe.style.left = "2.5%"
        iframe.style.top = "2%"
        iframe.style.border = "0px";
        document.body.appendChild(iframe)
        iframe.style.zIndex = 999999;
        iframe.width = "95%";
        iframe.height = "95%";
        iframe.style.boxShadow = "10px 10px 15px 0px rgba(0,0,0,0.75)"
    }
    document.body.appendChild(node);
}
addTfWidget(10,10, true)