<template>
  <div id="app">
    <ProductDataTable />
  </div>
</template>

<script>
import ProductDataTable from './components/ProductDataTable.vue'

export default {
  name: 'App',
  components: {
    ProductDataTable
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
