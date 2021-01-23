window.onload = function() {
  $("#skadeDropzone").dropzone({
    url: 'upload',
    maxFilesize: 2000,
    autoProcessQueue: false,
    uploadMultiple: true,
    parallelUploads: 100,
    maxFiles: 100,
    createImageThumbnails: false,
    init: function() {
        dzClosure = this;

        // for Dropzone to process the queue (instead of default form behavior):
        document.getElementById("submit").addEventListener("click", function(e) {
            console.log("submit button has been hit!")
            e.preventDefault();
            e.stopPropagation();
            dzClosure.processQueue();
        });

        //send all the form data along with the files:
        this.on("sendingmultiple", function(files, xhr, form) {
            form.append("yarascan", jQuery("#yarascan").val());
        });
        this.on('error', function(files, response) {
          alert(response);
        });
    }
  })
}