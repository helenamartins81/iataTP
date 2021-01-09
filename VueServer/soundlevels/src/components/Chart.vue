<template>
  <div class="small">
    <line-chart :chart-data="datacollection"></line-chart>
  </div>
</template>

<script>
  import LineChart from '../LineChart'

  export default {
      name: "SoundChart",
    components: {
      LineChart
    },
    props: ['soundvalue'],
    data () {
      return {
        datacollection: null,
        time : 0,
        //lastvalue : this.soundvalue,
        values : [],
        timevalues: [],
        hexcolour: '#42f590'
      }
    },
    mounted () {
      this.fillData()
    },
    computed: {
      colour() {
        return this.soundvalue > 50 ? '#f54242' : '#42f590';
      }
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: this.timevalues,
          datasets: [
            {
              label: 'Sound Value',
              backgroundColor: this.colour,
              data: this.values
            }
          ]
        }
        
        this.time += 10;
        this.timevalues.push(this.time);
        this.values.push(this.soundvalue);
        
        console.log(this.soundvalue);
        
        setTimeout(() => this.fillData(), 10000);
      }
    }
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
