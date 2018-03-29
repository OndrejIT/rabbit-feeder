{% args web_url, cam_stream_url %}

<!doctype html>
<html>
<head>
	<meta http-equiv="Content-Language" content="cs">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/css/toastr.min.css" />
	<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/toastr.js/latest/js/toastr.min.js"></script>
	<title>&#128007; Rabbit feeder &#128007;</title>

	<style type="text/css">
		.center {
			text-align: center;
		}

		body {
			background-color: #020101b3;
			color: #a7a7a7;
		}

		.button {
			padding: 20px;
			cursor: pointer;
			font-weight: bold;
			font-size: 150%;
			background: #FCE374;
			color: #705D07;
			border: 1px solid #C9AE34;
			border-radius: 10px;
			padding: 11px 50px 11px 50px
		}

		.button:hover {
			background: #FFBD00;
		}
	</style>

	<script>
		function get_resources(resource){
			if (resource !== 'light') {
				toastr["info"]("In progress", resource);
			}

			$.ajax({
				url: "{{ web_url }}/resources",
				dataType: "json",
				type: "post",
				contentType: "application/json",
				data: {"resource": resource},

				success: function(data, status, error){
					toastr["success"](data["status"], data["resource"]);
				},
				error: function(data, status, error){
					toastr["error"](error, "Resource");
				}
			});
		};

		toastr.options = {
			"closeButton": true,
			"debug": false,
			"newestOnTop": true,
			"progressBar": true,
			"positionClass": "toast-top-center",
			"preventDuplicates": false,
			"onclick": null,
			"showDuration": "300",
			"hideDuration": "1000",
			"timeOut": "3000",
			"extendedTimeOut": "1000",
			"showEasing": "swing",
			"hideEasing": "linear",
			"showMethod": "fadeIn",
			"hideMethod": "fadeOut"
		}		
	</script>
</head> 

<body>
	<a href="https://github.com/OndrejIT/rabbit-feeder"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png" alt="Fork me on GitHub"></a>
	<div class="center">
		<h1>
			&#128007; Rabbit feeder &#128007;
		</h1>
		<img src="{{ cam_stream_url }}">
		<p>
			<a onclick="get_resources('light')" class="button">Light</a>
			<a onclick="get_resources('food')" class="button">Food</a>
			<a onclick="get_resources('water')" class="button">Water</a>
		</p>
	</div>
</body>
</html>
