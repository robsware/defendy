$filename = 'renameDevice.txt';
$eachlines = file($filename, FILE_IGNORE_NEW_LINES);//create an array
echo '<select name="value" id="value">';
foreach($eachlines as $lines){
    echo "<option>{$lines}</option>";
}
echo '</select>';