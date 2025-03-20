<template>
    <div class="login">
      <h2>登录</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <input type="text" v-model="username" placeholder="用户名" required>
          </div>
        <div class="form-group">
          <input type="password" v-model="password" placeholder="密码" required>
          </div>
        <button type="submit">登录</button>
        <p>
          还没有账号？
          <router-link to="/register">立即注册</router-link>
        </p>
      </form>
    </div>
  </template>
  <script setup lang="ts">
    import { ref } from 'vue'
    import { useRouter } from 'vue-router'
  
    const router = useRouter()
    const username = ref('')
    const password = ref('')
  
    const handleLogin = () => {
      // TODO: 实现登录逻辑
      console.log('登录信息：', {
        username: username.value,
        password: password.value
      })
    }
  </script>
  <style scoped>
    .login {
      max-width: 400px;
      margin: 40px auto;
      padding: 20px;
    }
  
    .form-group {
      margin-bottom: 15px;
    }
  
    input {
      width: 100%;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
    }
  
    button {
      width: 100%;
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
  
    button:hover {
      background-color: #45a049;
    }
  </style>
  