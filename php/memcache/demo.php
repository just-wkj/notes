<?php
//phpinfo();

$mc = new Memcache();
$mc->connect("localhost", 11211);

$mc->set('key', 'Hello Memcached', 0, 600);
$val = $mc->get('key');
echo $val;
?>
