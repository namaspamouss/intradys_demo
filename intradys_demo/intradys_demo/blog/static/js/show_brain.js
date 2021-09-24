var canvas = document.getElementById("canvas");
var engine = new BABYLON.Engine(canvas, true);

function get_color_setting() {
    return $.ajax({
        url: "api/get_color_setting",
        dataType: "json"
    })

}

// here the doc for Load function: //doc.babylonjs.com/typedoc/classes/babylon.sceneloader#load
// a "static" template tag should be used to get .babylon model
// to be able to work in a prod env
BABYLON.SceneLoader.Load("/static/image/", "brain.babylon", engine, function (scene) {
    //as this .babylon example hasn't camera in it, we have to create one
    get_color_setting().done(function (data) {
        var camera = new BABYLON.ArcRotateCamera("Camera", 1, 1, 200, new BABYLON.Vector3(0, 0, 0), scene);
        camera.attachControl(canvas, false);
        camera.wheelPrecision = 10

        var light = new BABYLON.HemisphericLight("HemiLight", new BABYLON.Vector3(0, 150, 0), scene);

        // colors are in hex value (for an easier adaptation with css templates)
        light.diffuse = new BABYLON.Color3.FromHexString(data["chosen_color"]);

        scene.clearColor = new BABYLON.Color3(1, 1, 1);
        scene.ambientColor = new BABYLON.Color3.White();

        engine.runRenderLoop(function () {
            scene.render();
        });
        // resize method allow a responsive layout
        window.addEventListener("resize", function () {
            engine.resize();
        });

        $(".btn").click(function () {
        var chosen_color = this.id
        $.ajax({
            url: "api/set_color_setting",
            data: {
                "chosen_color": chosen_color
            },
            dataType: "json",
            success: function (data) {
                console.log(data["state"])
                get_color_setting().done(function (data) {
                    console.log(data["chosen_color"])
                    light.diffuse = new BABYLON.Color3.FromHexString(data["chosen_color"]);
                    
                })
            }
        })
    })
    })

    


});
