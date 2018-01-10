<<template>
    <div id="container"></div>
</template>
<script>
import BpmnViewer from 'bpmn-js'
export default {
    mounted:function(){  
    this.init()  
  },  
  methods:{  
    init:function () {
        let xml; // my BPMN 2.0 xml
        var viewer = new BpmnViewer({ container: '#container' });
        
        viewer.importXML(xml, function(err) {
            if (err) {
                console.log('error rendering', err);
            } else {
                console.log('rendered');
            }
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