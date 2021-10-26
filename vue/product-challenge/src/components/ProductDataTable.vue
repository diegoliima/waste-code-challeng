<template>
  <div class="p-container">
    <DataTable :value="products" dataKey="id" :filters="filters" responsiveLayout="scroll">
      <template #header>
          <div class="p-d-flex p-jc-between p-ai-center">
              <h5 class="p-m-0">Products</h5>
              <span class="p-input-icon-left p-ac-end">
                  <i class="pi pi-search" />
                  <InputText v-model="filters['global']" placeholder="Global Search" />
              </span>
          </div>
      </template>
      <Column v-for="col of columns" :field="col.field" :header="col.header" :key="col.field">
        <template #body="slotProps">
              {{slotProps.data[col.field]}}
          </template>
          <template #filter>
              <InputText type="text" v-model="filters[col.field]" class="p-column-filter" :placeholder="col.placeholder" />
          </template>
      </Column>
      <Column field="available_units" header="Available Units">
          <template #body="slotProps">
              <span class="p-input-icon-left">
                <i class="pi pi-sliders-v" />
                <InputText type="text" v-model="slotProps.data.available_units" class="p-inputtext-sm" placeholder="Edit Available Units"/>
              </span>
          </template>
      </Column>
  </DataTable>
  </div>
</template>

<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';

export default {
  name: 'ProductDataTable',
  components: {
    DataTable,
    InputText,
    Column
  },
  data() {
        return {
            filters: {},
            products: [
                {id: 1, product: "Apple granny smith", package: "40 LB", available_units: 3000.65, category: "Fruits", last_update: "2021-05-10"},
                {id: 2, product: "Banana green", package: "7 CT", available_units: 123.8, category: "Fruits", last_update: "2021-06-10"},
                {id: 3, product: "Pineaple crownless", package: "7 CT", available_units: 120, category: "Fruits", last_update: "2021-07-10"},
                {id: 4, product: "Banan green tip", package: "8 CT", available_units: 2987.98, category: "Fruits", last_update: "2021-08-10"},
                {id: 5, product: "Red Tomatos", package: "40 LB", available_units: 5671.87, category: "Vegetables", last_update: "2021-09-10"},
                {id: 6, product: "Orange", package: "10 LB", available_units: 1987.8, category: "Fruits", last_update: "2021-10-10"},
                {id: 7, product: "Lettuce", package: "10 LB", available_units: 2000, category: "Vegetables", last_update: "2021-10-10"},
            ],
            columns: [
              {field: 'id', header: "Item Code", placeholder: "Search by item code"},
              {field: 'product', header: "Product", placeholder: "Search by product"},
              {field: 'package', header: "Package", placeholder: "Search by package"},
              {field: 'available_units', header: "Available Units", placeholder: "Search by available units"},
              {field: 'category', header: "Category", placeholder: "Search by category"},
              {field: 'last_update', header: "Last Update", placeholder: "Search by last update"},
            ]
        }
    },
    methods: {
        filterDate(value, filter) {
            if (filter === undefined || filter === null || (typeof filter === 'string' && filter.trim() === '')) {
                return true;
            }

            if (value === undefined || value === null) {
                return false;
            }

            return value === this.formatDate(filter);
        },
        formatDate(date) {
            let month = date.getMonth() + 1;
            let day = date.getDate();

            if (month < 10) {
                month = '0' + month;
            }

            if (day < 10) {
                day = '0' + day;
            }

            return date.getFullYear() + '-' + month + '-' + day;
        }
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
