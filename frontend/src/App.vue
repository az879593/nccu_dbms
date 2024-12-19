<script setup>
</script>

<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand mb-0 h1 d-flex align-items-center">
          <svg 
            xmlns="http://www.w3.org/2000/svg" 
            width="25" 
            height="25" 
            viewBox="0 0 448 512" 
            class="me-2">
            <path 
              fill="white" 
              d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"
            />
          </svg>
          BookCycle
        </router-link>

        <!-- Navbar 選單 -->
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/book" class="nav-link fw-bold text-white">書籍</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/comments" class="nav-link fw-bold text-white">留言板</router-link>
            </li>
          </ul>

          <!-- User -->
          <div class="ms-auto">
            <router-link to="/user" class="nav-link">
              <svg 
                xmlns="http://www.w3.org/2000/svg" 
                width="25"
                height="25"
                viewBox="0 0 448 512"
                fill="white">
                <path 
                  d="M304 128a80 80 0 1 0 -160 0 80 80 0 1 0 160 0zM96 128a128 128 0 1 1 256 0A128 128 0 1 1 96 128zM49.3 464l349.5 0c-8.9-63.3-63.3-112-129-112l-91.4 0c-65.7 0-120.1 48.7-129 112zM0 482.3C0 383.8 79.8 304 178.3 304l91.4 0C368.2 304 448 383.8 448 482.3c0 16.4-13.3 29.7-29.7 29.7L29.7 512C13.3 512 0 498.7 0 482.3z"
                />
              </svg>
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <!-- 主要內容區域 -->
    <div class="container mt-4">
      <router-view />
    </div>
  </div>
</template>


<style>
</style>
