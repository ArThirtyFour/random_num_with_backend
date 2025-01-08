<template>
<h1>Привет! Это це маня саня для рандома</h1>
<hr>
<h5>Написана она на Flask + Vue</h5>
<h5>Пробуй вводи авось повезет</h5>
<Input/>
</template>

<style>
hr {
  color:white
}
h1 {
  text-align: center;
  font-family: 'Courier New', Courier, monospace;
  color: white;
  font-size: 30px;
}

h5 {
  font-family: 'Courier New', Courier, monospace;
  text-align: center;
  color: white;
  font-size: 30px;

}
</style>

<script>
import Input from './components/Input.vue'
export default {
  components : {Input}
}
</script>