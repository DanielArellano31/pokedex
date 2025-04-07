import { registerRootComponent } from 'expo';
import { createNativeStackNavigator } from '@react-navigation/native';
import App from './App';
import Register from './Register';

// registerRootComponent calls AppRegistry.registerComponent('main', () => App);
// It also ensures that whether you load the app in Expo Go or in a native build,
// the environment is set up appropriately
const Stack = createNativeStackNavigator();

export default function Main() {
    return (
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Home">
            <Stack.Screen name="Home" component={App}  />
            <Stack.Screen name="Register" component={Register}  />
           
        </Stack.Navigator>
      </NavigationContainer>
    );
  }


registerRootComponent(App);
