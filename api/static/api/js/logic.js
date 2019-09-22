    var filePath = "";


        $(document).ready(function () {

            $("#uploadFolder").click(function (event) {

                //stop submit the form, we will post it manually.
                event.preventDefault();

                // Get form
                var form = $('#fileUploadForm')[0];

                // Create an FormData object
                var data = new FormData(form);

                data.append("info", "");

                $.ajax({
                    type: "POST",
                    enctype: 'multipart/form-data',
                    url: "/dialogueBox/",
                    data: data,
                    processData: false,
                    contentType: false,
                    cache: false,
                    timeout: 600000,
                    success: function (data) {

                        filePath = data;
                        $("#selectedFolder").text("Selected folder: " + data + "/");
                    },
                    error: function (e) {

                    }
                });

            });

            $("#btnSubmit").click(function (event) {
                $("#result").text("Processing...");

                //stop submit the form, we will post it manually.
                event.preventDefault();

                // Get form
                var form = $('#fileUploadForm')[0];

                // Create an FormData object
                var data = new FormData(form);

                data.append("path", filePath);
                data.append("aa", "bb");

                // If you want to add an extra field for the FormData
                //data.append("CustomField", "This is some extra data, testing");

                // disabled the submit button

                $("#btnSubmit").prop("disabled", true);

                $.ajax({
                    type: "POST",
                    enctype: 'multipart/form-data',
                    url: "/upload/",
                    data: data,
                    processData: false,
                    contentType: false,
                    cache: false,
                    timeout: 600000,
                    success: function (data) {

                        $("#result").text(data);
                        console.log("SUCCESS : ", data);
                        $("#btnSubmit").prop("disabled", false);

                    },
                    error: function (e) {

                        // {#$("#result").text(e.responseText);#}
                        // {#console.log("ERROR : ", e);#}
                        // {#$("#btnSubmit").prop("disabled", false);#}

                    }
                });

            });


        });