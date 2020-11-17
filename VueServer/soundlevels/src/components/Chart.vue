<template>
  <div class="small">
    <line-chart :chart-data="datacollection"></line-chart>
  </div>
</template>

<script>
  import LineChart from '../LineChart'

  export default {
    components: {
      LineChart
    },
    data () {
      return {
        datacollection: null,
        time : 0,
        values : [],
        timevalues: []
      }
    },
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: this.timevalues,
          datasets: [
            {
              label: 'Sound Value',
              backgroundColor: '#f87979',
              data: this.values
            }
          ]
        }
        this.time += 10;
        this.timevalues.push(this.time);
        this.values.push(this.getRandomInt());
        console.log(this.values);
        setTimeout(() => this.fillData(), 5000);
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
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
