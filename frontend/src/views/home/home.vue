<<template>
<div>
    <Row :gutter="16">
        <Col span="18">
            <Carousel autoplay v-model="value2">
            <CarouselItem>
                <div class="demo-carousel">1</div>
            </CarouselItem>
            <CarouselItem>
                <div class="demo-carousel">2</div>
            </CarouselItem>
            <CarouselItem>
                <div class="demo-carousel">3</div>
            </CarouselItem>
            <CarouselItem>
                <div class="demo-carousel">4</div>
            </CarouselItem>
        </Carousel>
        </Col>
        <Col span="6">
            <Card>
                <p slot="title">登录</p>
                <Input v-model="loginname">
                    <span slot="prepend">登录：</span>
                </Input>
                <br>
                <Input v-model="passwd">
                    <span slot="prepend">密码：</span>
                </Input>
            </Card>
        </Col>
    </Row>   
</div>
</template>
<script>
    export default {
        data() {
            return {
            legendArr: [],
            color: this.$store.state.color,
            myChart: {},
            geoCoordMap: {},
            name: '散点图'}
        },
    }
</script>