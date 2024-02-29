var showLoadingScreen = function() {
    let loading_ele = $('#loading');
    loading_ele.css('display', 'block');
    setTimeout(function() {
        loading_ele.css('opacity', '1');
    }, 10);
};

var cppReportProgress = function(x) {
    let prog_ele = $("#load-progress");
    prog_ele.css("width", x + "%");
    prog_ele.attr("aria-valuenow", x);
    if (x > 100.0) {
        let loading_ele = $('#loading');
        setTimeout(function() {
            loading_ele.css('opacity', '0');
            setTimeout(function() {
                loading_ele.css('display', 'none');
            }, 600);
        }, 50);
        guiLoadTreeUpdate();
        Volrend.mesh_set_visible(i, false);
        populateLayers();
        // #! add to loading time
        var a = document.getElementById('load-time-val');
        a.innerText="File loaded in: "+(performance.now() - startTime).toFixed(2) + "ms";
        $('#div-load-time').css({'background-color': 'white'});

        var memoryUsage = performance.memory;
        // var b=document.getElementById('heaptotal-val');
        // b.innerText=("Total Heap Size: "+(memoryUsage.totalJSHeapSize / (1024 * 1024)).toFixed(2)+"MB");
        // $('#div-heaptotal').css({'background-color': 'white'});

        var c=document.getElementById('heapused-val');
        c.innerText=("Used Heap Size: "+(memoryUsage.usedJSHeapSize / (1024 * 1024)).toFixed(2)+"MB ("+(100 * memoryUsage.usedJSHeapSize / memoryUsage.totalJSHeapSize).toFixed(2)+"%)");
        $('#div-heapused').css({'background-color': 'white'});

        // var d=document.getElementById('heaplimit-val');
        // d.innerText=("Heap Size Limit: "+(memoryUsage.jsHeapSizeLimit / (1024 * 1024)).toFixed(2)+"MB");
        // $('#div-heaplimit').css({'background-color': 'white'});

        // #! end of edit here
    } else {
        prog_ele.text(x.toFixed(2));
    }
};

var cppUpdateFPS = function(fps) {
    $('#fps-counter-val').text(fps.toFixed(2));
};

var onResizeCanvas = function() {
    let canvas = document.getElementById("canvas");
    let height = window.innerHeight - $('#header').outerHeight() - 7;
    let width = window.innerWidth;
    canvas.width = width;
    canvas.height = height;
    Volrend.on_resize(width, height);
};

var Volrend = {
    preRun: [],
    postRun: [],
    print: (function() {})(),
    printErr: function() {},
    canvas: (function() {
        var canvas = document.getElementById('canvas');
        canvas.addEventListener("webglcontextlost", function(e) {
            e.preventDefault(); }, false);
        return canvas;
    })(),
    setStatus: function() {},
    totalDependencies: 0,
    monitorRunDependencies: function() {},
    onRuntimeInitialized: function() { $(document).ready(onInit); },
    set_title: function(title) {
        $('#navbar-title').text(title);
        document.title = title + " - PlenOctree Viewer";
    },
};
