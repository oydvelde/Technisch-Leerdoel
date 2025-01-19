<template>
  <div id="app">

    <h2 style="color: blueviolet">Overzicht</h2>
    <ul>
      <li v-for="item in itemList" :key="item.id">
        <p style="color: crimson">{{ item.eventId }} - {{ item.eventName }}</p>
      </li>
    </ul>

    <h2>Naam toevoegen</h2>
    <form @submit.prevent="postName">
      <input v-model="newName" placeholder="Voer een naam in"/>
      <button type="submit">Toevoegen</button>
    </form>
  </div>
</template>

<script>
const url = 'localhost:5050';

export default {
  name: 'App',
  components: {
  },
  data() {
    return {
      itemList: [],
      newName: ''
    };
  },
  created() {
    this.fetchList();
  },
  methods: {
    async fetchList() {
      try {
        const response = await fetch(`http://${url}/events`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        this.itemList = await data;
      } catch (error) {
        console.error('Error fetching list:', error);
      }
    },
    async postName() {
      if (!this.newName) return;
      try {
        const response = await fetch(`http://${url}/event`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({eventName: this.newName})
        });
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        this.fetchList()
      } catch (error) {
        console.error('Error posting name:', error);
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>