<template>
  <v-layout align-center justify-center class="pacman" style="padding:20px; text-align:center">
          <p style="letter-spacing: 3vw;margin:4%; width: 100%;">
              ● ● ● ● ● ● ● ● ● ● ●</p>
          <v-flex class="lectangle" style="padding:30px;position: absolute;width: 100%;">
          </v-flex> 
          <v-flex style="position: absolute;width: 100%;">
            <img src="../../assets/pacman-eating.gif" style="width: 50px;height: 50px;">
          </v-flex>
      </v-layout>
</template>

<style>
.pacman>div{
	opacity:0;
	animation: myPacManAnimation 8s ease;
}
.pacman>p{
	opacity:0;
	animation: myPotAnimation 8s ease;
}
 .pacman>.lectangle{
	 opacity:0;
  background:white;
 animation:myEatAnimation 7s ease;
 }
@keyframes myPotAnimation {
	0%{opacity:1;}
	80%{opacity:1;}
	90%{opacity:0;}
} 
 @keyframes myEatAnimation {
	0%{transform:translateX(-90%); opacity:1;}
	100%{transform:translateX(-10%); opacity:1;}
} 
	
@keyframes myPacManAnimation {
	0%{transform:translateX(-40%); opacity:1;}
	90%{transform:translateX(40%); opacity:1;}
	95%{transform:translateX(100%); opacity:0;}
}
</style>
