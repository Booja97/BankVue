<template>
  <div id="app">
    <div id="nav">
      <h2>Bank Management</h2>
    </div>
    <router-view/>
  </div>
</template>

<style  scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color:#191919;
  margin-left: auto;
  margin-right: auto;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #38b4f2;

    &.router-link-exact-active {
      color: #38b4f2;
    }
  }

}
</style>
