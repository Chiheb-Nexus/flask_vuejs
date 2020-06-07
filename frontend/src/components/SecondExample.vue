<template>
    <div class="container" style="margin-left: 30px; margin-rigt: 30px" >
        <div class="row align-items-center justify-content-center" style="margin-bottom: 10px">
            <b-button variant="info" v-on:click="refreshGrid">Refresh</b-button>
        </div>
        <ag-grid-vue :style="{width, height}"
                    class="ag-theme-alpine"
                    :columnDefs="columnDefs"
                    :rowData="rowData"
                    rowSelection="multiple">
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
                rowData: [],
                width: this.getGridWidth(),
                height: this.getGridHeight()
            }
        },
        components: {
            AgGridVue
        },
        beforeMount() {
            this.columnDefs = [
                {headerName: 'Name', field: 'name', checkboxSelection: true},
                {headerName: 'Track', field: 'track'},
                {headerName: 'Artist', field: 'artist'},
                {headerName: 'Album', field: 'album'}
            ];
        },
        methods: {
            fetchData(){
                return fetch('/api/v1/second-example/').then(result => result.json()).then(
                    rowData => this.rowData = rowData
                );
            },
            getGridWidth(){
                return window.innerWidth * 8/9 + 'px'
            },
            getGridHeight(){
                return window.innerHeight * 1/2 + 'px'
            },
            refreshGrid(){
                return this.fetchData()
            }
        }
    }
</script>

<style>
</style>