import { StatusBar } from 'expo-status-bar';
import { Image, Pressable, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';

export default function Register() {
  return (
   
   <View style={styles.container}>
      <Image source={{uri:"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png"}} 
      height={200} 
      width={200}/>
      <View>{/* Container form*/}
         <Text style={styles.title}>Iniciar sesion</Text>  
         <Text style={styles.label}>Nombre:</Text>
         <TextInput style ={styles.input}/>
         <Text style={styles.label}>Correo:</Text>
         <TextInput style ={styles.input}/>
         <Text style={styles.label}>Contraseña:</Text>
         <TextInput style ={styles.input}/>
         <Pressable style={styles.button}> 
          <Text style={styles.button.textButton}>Registrar</Text>
         </Pressable>
        
      </View>
      </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex:1,
    backgroundColor: 'white',
    padding:"10px",
    alignItems: 'center',
    justifyContent: 'center',
  },
  title:{
    fontSize:30,
    fontWeight:"bold"
  },
  label:{
    fontSize:20,
    fontWeight:"bold"
  },
  input:{
    borderRadius:10,
    borderWidth:2,
    borderColor:"black",
    fontSize:15,
    height:25,
    width:"auto"
  },
  button:{
    backgroundColor:"red",
    width:"auto",
    height:30,
    borderRadius:10,
    marginTop:15,
    alignItems:'center',
    textButton:{
    color:"black",
    fontSize:20,
    fontWeight:"bold",
    
    }
  },
  footer:{
    justifyContent:"space-between",
    text:{fontSize:15 }    
  }
});
