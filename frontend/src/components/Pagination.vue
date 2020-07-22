<template>
  <div class="post-pagination d-flex justify-content-center">
    <template v-if="isPaginated">
      <BPagination
        v-model="currentPageModel"
        :per-page="perPage"
        :total-rows="count"
      />
    </template>

    <!-- {{ currentPage }} -->
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    count: {
      type: Number,
      required: true,
    },
    currentPage: {
      type: Number,
      default: 1,
    },
    perPage: {
      type: Number,
      default: 10,
    },
  },
  computed: {
    currentPageModel: {
      get() {
        return this.currentPage;
      },
      set(value) {
        this.$emit("pageChanged", value);
      },
    },
    isPaginated() {
      return this.count > this.perPage;
    },
  },
};
</script>

<style scoped>
.post-pagination {
  margin-top: 30px;
}
.post-pagination >>> .pagination .page-item .page-link {
  background-color: transparent;
  font-size: 14px;
  color: #000;
  box-shadow: none;
  border: 1px solid rgb(0, 2, 7);
  border-radius: 5px;
}
.post-pagination >>> .pagination .page-item.active .page-link {
  /* border-color: black; */
  color: #000;
  font-size: large;
  background-color: rgba(61, 61, 61, 0.278);
  font-weight: bold;
  border: 3px solid rgb(0, 2, 7);
}
.post-pagination >>> .pagination .page-item:active .page-link {
  box-shadow: rgba(37, 37, 37, 0.267);
}
.post-pagination >>> .pagination .page-item.disabled .page-link {
  display: none;
}
</style>
