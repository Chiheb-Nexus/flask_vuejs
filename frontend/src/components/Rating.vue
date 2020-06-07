<template>
  <div class="row align-items-center justify-content-center" style="margin-bottom: 20px">
    <b-form-rating class="w-25 form-control-lg" v-model="value"></b-form-rating>
    <p class="mt-2" style="margin-left: 20px">Value: {{ value }}</p><br />
  </div>
</template>

<script>
  export default {
    data() {
      return {
        value: null
      }
    }
  }
</script>