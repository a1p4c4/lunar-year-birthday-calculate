<?php 

    /**
     * Written by Aylmer
     * Function :解析出file路径下所有txt文件的json数据，写入到csv文件中
     * Date/Time:2021/06/27
    */

    function readFromFile(string $filename){
        try{
            $handle = fopen($filename, "r");
            $temp = fread($handle, filesize($filename));
            fclose($handle);
            return $temp;
        }
        catch(Exception $ex){
            return false;
        }
    }


    function saveToFile(string $filename, string $content){
        try{
            $handle = fopen($filename, "a");
            fwrite($handle, $content . "\n");
            fclose($handle);
            return;
        }
        catch(Exception $ex){
            return false;
        }
    }

    function renderJsonData(string $content){
        try{
            $temp = json_decode($content, true);
            $data = array();
            for($i=0;$i<count($temp['data'][0]['almanac']);$i++){
                $data[$i]['year']       = $temp['data'][0]['almanac'][$i]['year'];
                $data[$i]['month']      = $temp['data'][0]['almanac'][$i]['month'];
                $data[$i]['day']        = $temp['data'][0]['almanac'][$i]['day'];
                $data[$i]['lunarYear']  = $temp['data'][0]['almanac'][$i]['lunarYear'];
                $data[$i]['lunarMonth'] = $temp['data'][0]['almanac'][$i]['lunarMonth'];
                $data[$i]['lunarDate']  = $temp['data'][0]['almanac'][$i]['lunarDate'];
                $data[$i]['lMonth']     = $temp['data'][0]['almanac'][$i]['lMonth'];
                $data[$i]['lDate']      = $temp['data'][0]['almanac'][$i]['lDate'];
                $data[$i]['gzYear']     = $temp['data'][0]['almanac'][$i]['gzYear'];
                $data[$i]['gzMonth']    = $temp['data'][0]['almanac'][$i]['gzMonth'];
                $data[$i]['gzDate']     = $temp['data'][0]['almanac'][$i]['gzDate'];
                $data[$i]['animal']     = $temp['data'][0]['almanac'][$i]['animal'];
            }
            return $data;
        }
        catch(Exception $ex){
            return false;
        }        
    }

    for($i=1;$i<325;$i++){
        if(($temp = readFromFile("./file/1 (" . (string)($i) . ").txt")) !== false){
            $data = renderJsonData($temp);
            if($data !== false){
                for($j=0;$j<count($data);$j++){
                    saveToFile("./data.csv", $data[$j]['year'] . ',' . $data[$j]['month'] . ',' . $data[$j]['day'] . ',' . $data[$j]['lunarYear'] . ',' . $data[$j]['lunarMonth'] . ',' . $data[$j]['lunarDate'] . ',' . $data[$j]['lMonth'] . ',' . $data[$j]['lDate'] . ',' . $data[$j]['gzYear'] . ',' . $data[$j]['gzMonth'] . ',' . $data[$j]['gzDate'] . ',' . $data[$j]['animal']);
                }
                print("写入成功！(" . (string)($i) . ")\n");
            }else{
                print("解析失败。(" . (string)($i) . ")\n");
                exit();
            }
        }else{
            print("读取失败。(" . (string)($i) . ")\n");
        }
    }
    print("全部读取成功！")





?>