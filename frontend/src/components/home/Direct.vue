<template>
    <v-container>
        <v-row dense>
            <v-col
                v-for="(item, i) in items"
                :key="i"
                cols="12"
                xs="12" sm="2"
            >
                <center>
                    <v-avatar
                        class="ma-3"
                        size="125"
                        id="tag"
                    >
                        <v-img :src="item.src"></v-img>
                    </v-avatar>
                </center>
                <center id="font">{{item.title}}</center>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    data: () => ({
        items: [
            {
                title: "아이폰 XS, XR",
                src : "https://image.flaticon.com/icons/svg/2223/2223340.svg"
            },
            {
                title: "아이폰 7, 7+, 8",
                src : "https://image.flaticon.com/icons/svg/148/148998.svg"
            },
            {
                title: "아이폰 6 이하",
                src : "https://image.flaticon.com/icons/svg/164/164413.svg"
            },
            {
                title: "아이패드 프로",
                src : "https://image.flaticon.com/icons/svg/644/644425.svg"
            },
            {
                title: "아이패드 미니",
                src : "https://image.flaticon.com/icons/svg/273/273579.svg"
            },
            {
                title: "아이패드 에어",
                src : "https://image.flaticon.com/icons/svg/125/125271.svg"
            },
            {
                title: "갤럭시탭",
                src : "https://image.flaticon.com/icons/svg/204/204282.svg"
            },
            {
                title: "갤럭시 폴드",
                src : "https://www.flaticon.com/premium-icon/icons/svg/1796/1796311.svg"
            },
            {
                title: "갤럭시 S10",
                src : "https://image.flaticon.com/icons/svg/254/254040.svg"
            },
            {
                title: "갤럭시 노트",
                src : "https://image.flaticon.com/icons/svg/1373/1373263.svg"
            },
            {
                title: "갤럭시 그외",
                src : "https://image.flaticon.com/icons/svg/2152/2152553.svg"
            },
            {
                title: "삼성전자 제품",
                src : "https://image.flaticon.com/icons/svg/882/882747.svg"
            }
        ]
    })
}
</script>

<style>
#font {
  font-family: 'Cute Font', cursive;
  font-size: 30px;
}
#tag{
    background-color: rgb(233, 102, 102);
}

</style>