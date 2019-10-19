<?php
defined('IN_TS') or die('Access Denied.');

class article extends tsApp {

    //构造函数
    public function __construct($db) {
        $tsAppDb = array();
        include 'app/article/config.php';
        //判断APP是否采用独立数据库
        if ($tsAppDb) {
            $db = new MySql($tsAppDb);
        }

        parent::__construct($db);
    }

    //热门文章,1天，7天，30天
    /**
     * @param $day
     * @param int $cateid
     * @return mixed
     */
    public function getHotArticle($day, $cateid = 0) {
        $startTime = time() - ($day * 3600 * 24);
        $startTime = date('Y-m-d', $startTime);

        $endTime = date('Y-m-d');

        if ($day == 30) {
            $endTime = date('Y-m-d', time() - (7 * 3600 * 24));
        }

        if ($cateid) {
            $arr = "`cateid`='$cateid' and `count_view`>'0' and `addtime`>'$startTime' and `addtime`<'$endTime' and `isaudit`='0'";
        } else {
            $arr = "`addtime`>'$startTime' and `count_view`>'0' and `addtime`<'$endTime' and `isaudit`='0'";
        }

        $arrArticle = $this->findAll('article', $arr, 'addtime desc', 'articleid,title', 10);
        foreach ($arrArticle as $key => $item) {
            $arrArticle[$key]['title'] = tsTitle($item['title']);
        }

        return $arrArticle;
    }

    //推荐文章 $cateid
    /**
     * @param int $cateid
     * @return mixed
     */
    public function getRecommendArticle($cateid = 0) {

        if ($cateid) {
            $arr = array(
                'cateid' => $cateid,
                'isrecommend' => 1,
            );
        } else {
            $arr = array(
                'isrecommend' => 1,
            );
        }

        $arrArticle = $this->findAll('article', $arr, 'addtime desc', 'articleid,title', 10);
        foreach ($arrArticle as $key => $item) {
            $arrArticle[$key]['title'] = tsTitle($item['title']);
        }

        return $arrArticle;
    }

    /*
     * 是否文章作者
     */
    public function isArticleUser($articleid,$userid){
        $isUser = $this->findCount('article',array(
            'articleid'=>$articleid,
            'userid'=>$userid,
        ));

        if($isUser){
            return true;
        }else{
            return false;
        }

    }


    /**
     * 获取文章关联视频
     * @param $articleid
     * @return mixed
     */
    public function getArticleVideo($articleid){

        $arrVideoId = $this->findAll('article_video',array(
            'articleid'=>$articleid,
        ));

        $arrVideo = array();

        if($arrVideoId){
            foreach($arrVideoId as $key=>$item){
                $arrId[] = $item['videoid'];
            }

            $videoid = arr2str($arrId);

            $arrVideo = $this->findAll('video',"`videoid` in ($videoid)");

            foreach($arrVideo as $key=>$item){
                if($item['siteid']==1){
                    $arrVideo[$key]['iframe'] = "//v.qq.com/txp/iframe/player.html?vid=".$item['vid'];
                }elseif($item['siteid']==2){
                    $arrVideo[$key]['iframe'] = "//player.youku.com/embed/".$item['vid']."==";
                }elseif($item['siteid']==3){
                    $arrVideo[$key]['iframe'] = "//player.bilibili.com/player.html?aid=".$item['vid']."&page=1";
                }else{

                }
            }

        }

        return $arrVideo;

    }

}
