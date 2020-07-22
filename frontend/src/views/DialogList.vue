<template>
  <div>
    <div class="container">
      <div class="row mt-2">
        <div class="col-6">
          <button class="change-list in-l" @click="InListHandler">IN</button>
        </div>
        <div class="col-6">
          <button class="change-list out-l" @click="OutListHandler">OUT</button>
        </div>
      </div>
      <template>
        <div v-for="dialog in dialogItems" :key="dialog.id">
          <DialogListItem :dialog="dialog" />
        </div>
      </template>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

import DialogListItem from "@/components/dialog/DialogListItem";

export default {
  name: "Dialog",
  data: () => ({
    showList: "IN",
  }),
  components: {
    DialogListItem,
  },
  computed: {
    ...mapGetters("dialog", ["dialogInList", "dialogOutList"]),
    dialogItems() {
      let list = [];
      if (this.showList === "IN") {
        list = this.dialogInList;
      }
      if (this.showList === "OUT") {
        list = this.dialogOutList;
      }
      return list;
    },
  },
  mounted() {
    this.fetchDialogList();
  },
  methods: {
    ...mapActions("dialog", ["fetchDialogList"]),
    InListHandler(e) {
      const buttonIn = e.path[0];
      const parent = e.path[2];
      const buttonOut = parent.querySelector(".out-l");

      buttonIn.classList.add("change-list-active");
      buttonIn.classList.remove("change-list");

      buttonOut.classList.add("change-list");
      buttonOut.classList.remove("change-list-active");

      this.showList = "IN";
    },
    OutListHandler(e) {
      const buttonOut = e.path[0];
      const parent = e.path[2];
      const buttonIn = parent.querySelector(".in-l");

      buttonOut.classList.add("change-list-active");
      buttonOut.classList.remove("change-list");

      buttonIn.classList.add("change-list");
      buttonIn.classList.remove("change-list-active");

      this.showList = "OUT";
    },
  },
};
</script>

<style scoped>
.change-list {
  width: 100%;
  border: 3px solid rgb(0, 0, 0);
  background-color: rgba(54, 54, 54, 0.945);
  color: rgba(194, 194, 194, 0.911);
}
.change-list-active {
  color: rgba(0, 0, 0, 0.979);
  background-color: rgba(255, 255, 255, 0.89);
  font-size: x-large;
  width: 100%;
  border: 5px solid rgb(0, 0, 0);
  font-weight: bold;
}
</style>
