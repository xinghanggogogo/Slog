<template lang="html">
    <el-pagination
        :total = "400"
        :page-size = "100"
        :page-sizes = "100, 200, 300, 400"
        layout = "total, sizes, prev, next"
        @size-change = 'handlerSizeChange'
        @current-change = "handlerCurrentChange"
    >
    </el-pagination>
</template>

<script>
export default {
    name: 'el-test',
    data() {
        return {

        }
    },
    methods: {
        handlerSizeChange(total) {
            console.log(total)
        },
        handlerCurrentChange(page) {
            this.$store.dispatch('fetchshow', {cat: this.cat, page: page})
        }
    }
}
</script>

<style lang="css">
</style>
