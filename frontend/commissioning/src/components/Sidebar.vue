<template>
<!-- Sidebar Holder -->
<nav id="sidebar" v-bind:class="{ active: isActive }" v-on:toggleSidebar="toggleSidebar">
    <div class="sidebar-header">
        <h3>Bootstrap Sidebar</h3>
    </div>

    <ul class="list-unstyled components">
        <p>Dummy Heading</p>
        <li class="active">
            <a href="#homeSubmenu" data-toggle="collapse" aria-expanded="false">Home<span class="arrow"></span></a>
            <ul class="collapse list-unstyled" id="homeSubmenu">
                <li><a href="#">Home 1</a></li>
                <li><a href="#">Home 2</a></li>
                <li><a href="#">Home 3</a></li>
            </ul>
        </li>
        <li>
            <a href="#">About</a>
            <a href="#pageSubmenu" data-toggle="collapse" aria-expanded="false">Pages<span class="arrow"></span></a>
            <ul class="collapse list-unstyled" id="pageSubmenu">
                <li><a href="#">Page 1</a></li>
                <li><a href="#">Page 2</a></li>
                <li><a href="#">Page 3</a></li>
            </ul>
        </li>
        <li>
            <a href="#">Layout</a>
        </li>
        <li>
            <a href="#">Contact</a>
        </li>
    </ul>

    <ul class="list-unstyled CTAs">
        <li><a href="https://bootstrapious.com/tutorial/files/sidebar.zip" class="download">Download source</a></li>
        <li><a href="https://bootstrapious.com/p/bootstrap-sidebar" class="article">Back to article</a></li>
    </ul>
</nav>
</template>

<script>
import { EventBus } from '@/utils'
export default {
  data () {
    return {
      isActive: false
    }
  },
  methods: {
    toggleSidebar () {
      this.isActive = !this.isActive
    }
  },
  created: function () {
    EventBus.$on('toggleSidebar', this.toggleSidebar)
  },
  beforeDestroy: function () {
    EventBus.$off('toggleSidebar', this.toggleSidebar)
  }
}
</script>

