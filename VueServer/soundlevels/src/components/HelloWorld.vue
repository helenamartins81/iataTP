<template>
  <div class="hello">
    <h2>Sound Level: {{ value }} dB</h2>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data: () => ({
    value : ''
  }),
  props: {
    msg: String
  },
  methods: {
    getValue(){
      var v = this;
      
      fetch('https://io.adafruit.com/api/v2/Barca88/feeds/workshop-somanalog/data/last', {
        method: 'get',
        headers: {
          "X-AIO-Key": "aio_KgtP88Z5IAEdT78vSQOfTQ6Zj7xK"
        }
      })
      .then(function(response){
        return response.json();
      }) 
      .then(function (data) {
        v.value = parseInt(data.value);
      
        console.log('Request succeeded with JSON response', data.value);

        setTimeout(() => v.getValue(), 10000);
      })
      .catch(function (error) {
        console.log('Request failed', error);
      });
    }
  },
  created(){
    this.getValue();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
