new Vue({
    el: '#some_element'
})

Vue.compnent('my-compnent', {
    data()
})

Vue.component('child', {
    props: ['message'],
    template: '<span>{{message}}</span>'
})
<div>
    <input type="text" v-model='parent-msg'/>
    <br/>
    <child :message='parent-msg'></child>
</div>

<comp some-prop='1'></comp>
<comp :some-prop='1'></comp>

<my-component v-on:click.native='doTheThing'></my-component>

var parent = new Vue({
    el: '#parent'
})
var child = parent.$refs.profile
