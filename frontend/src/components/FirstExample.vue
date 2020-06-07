<template>
<div class="container" style="margin-left: 30px; margin-rigt: 30px" >
    <div class="row align-items-center justify-content-center" style="margin-bottom: 10px">
        <b-button variant="info" v-on:click="refreshGrid">Refresh</b-button>
    </div>
    <ag-grid-vue :style="{width, height}"
                 class="ag-theme-alpine"
                 :columnDefs="columnDefs"
                 :rowData="rowData">
    </ag-grid-vue>
</div>
</template>

<script>
    import {AgGridVue} from "ag-grid-vue";

    export default {
        name: 'App',
        data() {
            return {
                columnDefs: null,
                rowData: null,
                width: this.getGridWidth(),
                height: this.getGridHeight()
            }
        },
        components: {
            AgGridVue
        },
        beforeMount() {
            this.columnDefs = [
                {headerName: 'Name', field: 'name', sortable: true, filter: true},
                {headerName: 'Age', field: 'age', sortable: true, filter: true},
                {headerName: 'Exam1', field: 'exam1', sortable: true, filter: true},
                {headerName: 'Exam2', field: 'exam2', sortable: true, filter: true},
                {headerName: 'Exam3', field: 'exam3', sortable: true, filter: true},
                {headerName: 'Exam4', field: 'exam4', sortable: true, filter: true},
            ];
            this.fetchData()
        },
        methods:{
            getGridWidth(){
                return window.innerWidth * 8/9 + 'px'
            },
            getGridHeight(){
                return window.innerHeight * 1/2 + 'px'
            },
            fetchData(){
                return fetch('/api/v1/first-example/').then(result => result.json()).then(
                    rowData => this.rowData = rowData
                );
            },
            refreshGrid(){
                return this.fetchData()
            }
        }
    }
</script>