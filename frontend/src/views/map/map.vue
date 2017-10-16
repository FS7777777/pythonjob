<<template>
    <!--   定义地图显示容器   -->
    <div id="container"></div>
</template>
<script>
export default {
  mounted:function(){  
    this.init()  
  },  
  methods:{  
    init:function () {  
      var myLatlng = new qq.maps.LatLng(31.584617993869276, 120.29067993164062);  
      var myOptions = {  
        zoom: 12,  
        center: myLatlng,  
        mapTypeId: qq.maps.MapTypeId.ROADMAP  
      }  
      var map = new qq.maps.Map(document.getElementById("container"), myOptions);  
      //添加监听事件  
      qq.maps.event.addListener(map, 'click', function(event) {  
        console.log('您点击的位置为: [' + event.latLng.getLat() + ', ' +  
          event.latLng.getLng() + ']');  
      });  
    }  
  }  
}
</script>
<style>
#container{
    min-width:200px;
    min-height:400px;
}
</style>
