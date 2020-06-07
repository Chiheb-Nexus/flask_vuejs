<template>
    <div>
        <b-navbar type="dark" variant="dark">
            <b-navbar-nav>
            <b-nav-item to="/">Home</b-nav-item>
            <!-- Navbar dropdowns -->
            <b-nav-item-dropdown text="Pages" right>
                <b-dropdown-item :to="'first-example'">1st Example</b-dropdown-item>
                <b-dropdown-item :to="'second-example'">2nd Example</b-dropdown-item>
                <b-dropdown-item :to="'third-example'">3rd Example</b-dropdown-item>
            </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-navbar>
        <br/>
    </div>
</template>
<script>
    export default {
        name: 'App'
    }
</script>