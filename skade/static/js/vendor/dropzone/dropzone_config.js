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
        document.getElementById("submit-all").addEventListener("click", function(e) {
            e.preventDefault();
            e.stopPropagation();
            dzClosure.processQueue();
        });

        //send all the form data along with the files:
        this.on("sending", function(data, xhr, formData) {
            formData.append("yarascan", jQuery("#yarascan").val());
        });
        myDropzone.on('errormultiple', function(files, response) {
          alert(response);
        });
    }
  })
}