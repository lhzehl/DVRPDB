<template>
  <div>
    <div class="container">
      <div class="row">
        <router-link class="mx-auto mt-2 mb-2 btn-d" to="/dialog">Messages</router-link>
      </div>
    </div>
    <DialogDetailItem v-if="isExist" :dialog="dialogDetail" />
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import DialogDetailItem from "@/components/dialog/DialogDetailItem";
export default {
  name: "DialogDetail",
  components: {
    DialogDetailItem,
  },
  props: {
    id: {
      type: Number,
    },
  },
  watch: {
    "$route.params": {
      handler: "onDialogParamsChange",
      immediate: true,
      depp: true,
    },
  },
  methods: {
    ...mapActions("dialog", ["fetchDialogDetail"]),
    onDialogParamsChange({ id = this.id } = {}) {
      this.fetchDialogDetail(Number(id));
    },
  },
  computed: {
    ...mapGetters("dialog", ["dialogDetail"]),
    isExist() {
      return Boolean(this.dialogDetail.sender);
    },
  },
};
</script>

<style scoped>
.btn-d {
  color: rgba(250, 250, 250, 0.979);
  background-color: rgba(54, 54, 54, 0.678);
  width: 100%;
  border: 3px solid rgb(0, 0, 0);
}
</style>
