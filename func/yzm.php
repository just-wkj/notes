<?php
	/*
	 *	@Func		生成验证码图片
	 *	@Author		wkj
	 *	@CreateTime	2016/9/9
	 *  @Param 		$wdith 宽度
	 *  @Param 		$height 高度
	 *  @Param 		$count 长度
	 *  @UpdateTime
	 **/
	function build_auth_code_img( $width = 120, $height = 40, $count = 4 )
	{
		$randnum = "";
		if ( function_exists( "imagecreatetruecolor" ) && function_exists( "imagecolorallocate" ) && function_exists( "imagestring" ) && function_exists( "imagepng" ) && function_exists( "imagesetpixel" ) && function_exists( "imagefilledrectangle" ) && function_exists( "imagerectangle" ) )
		{
			$image = imagecreatetruecolor( $width, $height );
			$swhite = imagecolorallocate( $image, 255, 255, 255 );
			$sblack = imagecolorallocate( $image, 0, 0, 0 );
			imagefilledrectangle( $image, 0, 0, $width, $height, $swhite );
			imagerectangle( $image, 0, 0, $width, $height, $swhite );
			$i = 0;
			for ( ;	$i < 10; ++$i ){
				$sjamcolor = imagecolorallocate( $image, rand( 0, 120 ), rand( 0, 120 ), rand( 0, 120 ) );
				imagesetpixel( $image, rand( 0, $width ), rand( 0, $height ), $sjamcolor );
			}
			$i = 0;
			for ( ;	$i < $count; ++$i ){
				 //$randnum .= dechex( rand( 1, 15 ) );
			}

			mt_srand((double)microtime() * 1000000);
			for($i=0;$i<$count;$i++){
				$randval.= mt_rand(0,9);
			}

			$randnum = $randval;
			$_SESSION['yzm_code'] = $randnum;

			
			$widthx = floor( $width / $count );
			$i = 0;
			for ( ;	$i < strlen( $randnum ); ++$i ){
				$irandomcolor = imagecolorallocate( $image, rand( 50, 120 ), rand( 50, 120 ), rand( 50, 120 ) );
				imagestring( $image, 5, $widthx * $i + rand( 3, 5 ), rand( 3, 5 ), $randnum[$i], $irandomcolor );
			}
			
			ob_clean();
			header( "Pragma:no-cache" );
			header( "Cache-control:no-cache" );
			header( "Content-type: image/png" );
			imagepng( $image );
			imagedestroy( $image );
			return $randnum;
		} 
	}
?>