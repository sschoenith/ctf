<?php
function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }
    return $outText;
}


function saveData($d) {
    return base64_encode(xor_encrypt(json_encode($d)));
}

$defaultdata = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
echo saveData($defaultdata);
echo "\n";
?>

<?php
$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
$defaultdata = array("showpassword"=>"no", "bgcolor"=>"#ffffff");
$xorkey = json_encode($defaultdata) ^ base64_decode($cookie);
echo $xorkey;
?>

$defaultdata = array("showpassword"=>"no", "bgcolor"=>"#ffffff");
$newdata = array("showpassword"=>"yes", "bgcolor"=>"#ffffff");
echo strlen(json_encode($defaultdata));
echo strlen(json_encode($newdata));
