<template>
  <div class="row2">
    <CardRow/>
    <ChartRow/>
  </div>
</template>
<script>

import CardRow from "./cardrows";
import ChartRow from "./chartRow";
export default {
  components: {
    
    CardRow,
    ChartRow
  },
  data() {
    return {
      value6: ""
    };
  }
};
</script>
<style lang="scss" scoped>
.row2 {
  margin-top: 20px;
  padding-top: 20px;
  background: #fff;
}
</style>


   