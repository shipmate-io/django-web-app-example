<template>
  <div class="p-8">
    <h1 class="font-sans text-3xl font-bold">
      Welcome to the frontend
    </h1>
    <h2 class="mt-8">
      Here is a list of programming languages fetched from the backend:
    </h2>
    <div class="ml-4 mt-4">
      <p v-if="$fetchState.pending">
        Fetching data from backend...
      </p>
      <p v-else-if="$fetchState.error">
        An error occurred :(
      </p>
      <ul v-else class="ml-4 list-disc list-outside">
        <li v-for="programmingLanguage of programmingLanguages">
          {{ programmingLanguage.name }}
        </li>
      </ul>
    </div>
    <button @click="$fetch" class="mt-8 border px-3 py-1 rounded">Refresh</button>
  </div>
</template>

<script>
export default {
  data: () => ({
    programmingLanguages: []
  }),
  async fetch() {
    this.programmingLanguages = await this.$axios.$get('/api/programming-languages')
  }
}
</script>
