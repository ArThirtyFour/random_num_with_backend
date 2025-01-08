<template>
    <div class="input-container">
      <input type="number" placeholder="Первое число" v-model="first_num">
      <input type="number" placeholder="Второе число" v-model="second_num">
    </div>
    <div class="button-container">
      <button disabled v-if="message">{{ message }}</button>
      <button v-else @click="GetRandomNumber()">Получить число</button> 
      <p v-if="result == ''">{{ result }}</p>
      <p v-else>Результат : {{ result }}</p>
      <button @click='RemoveResult() 'v-if="result !=''">Стереть</button>
    </div>
   
    
  </template>
  
  <style>
  .input-container {
    display: flex;
    justify-content: space-between; 
  }
  
  input {
    text-align: center;
    background-color: rgba(2, 76, 76, 0.536);
    color: white;
    border: 3px solid black;
    border-radius: 10px;
    font-family: 'Courier New', Courier, monospace;
    font-size: 20px;
  }
  



  .button-container {
    display: flex; 
    justify-content: center; 
    align-items: center;
    margin-top: 10px; 
    flex-direction: column;
    gap: 10px;

}




  button:disabled {
    border: 3px solid black;
    border-radius: 10px;
    color:rgba(255, 255, 255, 0.525);
    background: rgba(2, 76, 76, 0.536)
  }

  button{
    border: 3px solid black;
    border-radius: 10px;
    color:rgb(255, 255, 255);
    background: rgba(2, 76, 76, 0.536);
    padding: 10px 20px; 
    width: 150px

}

  p {
    color: white;
    font-size: 30px;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif
  }
  </style>
  
  <script>

  import axios from 'axios';
  export default {
    data() {
      return {
        first_num: '',
        second_num: '',
        result: ''
      };
    },
    computed: {
      message() {
        if (this.first_num === '' || this.second_num === '') {
          return 'Введите числа!';
        } else if (this.first_num >= this.second_num) {
          return 'Первое число больше второго';
        }
        return '';
      }
    },
    methods: {
    GetRandomNumber() {
        axios.post('http://127.0.0.1:5000/api/get_random_number', new URLSearchParams({
            first_num: this.first_num,
            second_num: this.second_num
        }))
        .then(response => {
            this.result = response.data;
        })
        .catch(error => {
            console.error('Ошибка при получении случайного числа:', error);
        });
    },
    RemoveResult () {
        this.result = ''
    }
}

  }
  </script>
  