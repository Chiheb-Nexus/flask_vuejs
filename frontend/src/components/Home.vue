<template>
    <div>
        <Rating/>
        <FirstExample />
    </div>
</template>

<script>
import FirstExampleVue from './FirstExample.vue'
import Rating from './Rating.vue'


export default {
    components: {
        'Rating': Rating,
        'FirstExample': FirstExampleVue
    }
}
</script>