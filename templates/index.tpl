{% args url %}

<!doctype html>
<html>
<head>
	<meta http-equiv="Content-Language" content="cs">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<title>Králičí krmítko</title>

	<style type="text/css">
		.center {
			text-align: center;
		}

		body {
			background-color: #020101b3;
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
			$.ajax({
				url: "{{url}}/resources",
				dataType: "json",
				type: "post",
				contentType: "application/json",
				data: {"resource": resource},

				success: function(data, status, error){
					alert("ok");
				},
				error: function(data, status, error){
					alert("err");
				}
			});
		};
	</script>
</head> 

<body>
	<div class="center">
		<img src="https://www.thesun.co.uk/wp-content/uploads/2016/06/nintchdbpict000212879086.jpg?w=600">
		<p>
			<a onclick="get_resources('food')" class="button">Zrní</a>
			<a onclick="get_resources('water')" class="button">Voda</a>
		</p>
	</div>
</body>
</html>
