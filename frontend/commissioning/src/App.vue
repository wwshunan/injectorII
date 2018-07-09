<template>
  <div id="app">
    <app-header></app-header>
    <div class="wrapper">
      <app-sidebar></app-sidebar>
      <div class="container-fluid">
        <app-breadcrumb></app-breadcrumb>
        <router-view/>
      </div>
    </div>
  </div>
</template>

<script>
import AppSidebar from '@/components/Sidebar'
import AppHeader from '@/components/Header'
import AppBreadcrumb from '@/components/Breadcrumb'

export default {
  name: 'App',
  components: { AppSidebar, AppHeader, AppBreadcrumb }
}
</script>

<style>
</style>
