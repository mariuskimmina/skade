Dropzone.options.fileDropzone = {
    paramName: "file",
    maxFilesize: 500000,
    timeout: 0,
    createImageThumbnails: false,
    init: function() {
      this.on('queuecomplete', function () {
        location.reload()
      });
      this.on("maxfilesexceeded", function(file) {
        this.removeAllFiles();
        this.addFile(file);
      });
    },   
};