<template>
  <div>
    <div class="row">
      <div class="col-6 p-left">
        <p v-if="profile.name">Name:</p>
        <p class="mt-2 p-left">Username:</p>
        <p class="mt-2 p-left">DOB:</p>
        <p class="mt-2 p-left">Photo:</p>
      </div>
      <div class="col-6 p-right">
        <p  v-if="profile.name" class="mt-2">{{ profile.name }}</p>
        <p class="mt-2 p-right">{{ profile.username || "" }}</p>
        <p class="mt-2 p-right">{{ localeDate }}</p>
        <img class="mt-2 profile-image" :src="profile.image" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "UsersProfile",
  props: {
    profile: {
      type: Object,
      required: true,
    },
  },
  computed:{
    localeDate(){
      return new Date(this.profile.dob).toLocaleDateString();
    }
  }
};
</script>

<style scoped>
.profile-image{
  border-radius: 5rem;
  max-width: 200px;
  

}
.p-left{
  border: solid 2px steelblue;
}
.p-right{
  border: solid 2px steelblue;
}
</style>
